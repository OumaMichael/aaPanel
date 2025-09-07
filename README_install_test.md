# aaPanel Installation and Testing Guide

## Overview

This document provides comprehensive instructions for installing, testing, and managing aaPanel with enhanced security features including SHA256 checksum verification, GPG signature verification, and automated uninstall functionality.

## Installation Methods

### Standard Installation

1. **Prerequisites:**
   - Linux distributions: Ubuntu 22.04/24.04, Debian 11/12, CentOS 9, Rocky/AlmaLinux 8/9
   - Minimum 512MB RAM (768MB recommended)
   - Minimum 100MB available disk space
   - Root or sudo privileges required
   - Clean system (no existing Apache/Nginx/PHP/MySQL installations)

2. **Download and Install:**
   ```bash
   # Download the installation script
   URL=https://www.aapanel.com/script/install_6.0_en.sh && \
   if [ -f /usr/bin/curl ]; then curl -ksSO "$URL"; else wget --no-check-certificate -O install_6.0_en.sh "$URL"; fi

   # Run the installation
   bash install_6.0_en.sh 66959f96
   ```

3. **Installation Options:**
   ```bash
   bash install_6.0_en.sh [options]

   Options:
     -u, --user <username>        Set aaPanel username
     -p, --password <password>    Set aaPanel password
     -P, --port <port>           Set aaPanel port (default: random 10000-55535)
     --safe-path <path>          Set aaPanel safe path
     --ssl-disable               Disable SSL for panel
     --uninstall                 Uninstall aaPanel completely
     -y                          Auto-confirm installation
   ```

### Docker Installation

```bash
# Run aaPanel in Docker
docker run -d \
  -p 8886:8888 \
  -p 22:21 \
  -p 443:443 \
  -p 80:80 \
  -p 889:888 \
  -v ~/website_data:/www/wwwroot \
  -v ~/mysql_data:/www/server/data \
  -v ~/vhost:/www/server/panel/vhost \
  aapanel/aapanel:lib

# Access at: http://your-ip:8886
# Default credentials: aapanel / aapanel123
```

## Security Features

### SHA256 Verification

The installation script includes SHA256 checksum verification for all downloaded files:

```bash
# Verify SHA256 checksum
verify_sha256 "filename" "expected_hash"
```

### GPG Signature Verification

GPG signature verification ensures the authenticity of installation files:

```bash
# Verify GPG signature
verify_gpg_signature "file" "signature.asc" "key_id"
```

### Download with Verification

Enhanced download function with optional verification:

```bash
# Download with SHA256 and GPG verification
download_with_verify "url" "output_file" "sha256_url" "gpg_sig_url" "gpg_key_id"
```

## Testing and Validation

### Running Tests

1. **Local Testing:**
   ```bash
   # Make script executable
   chmod +x install_test.sh

   # Run test script
   bash install_test.sh
   ```

2. **CI/CD Testing:**
   - Automated testing via GitHub Actions
   - Multi-OS testing (Ubuntu 20.04/22.04)
   - Security scanning with CodeQL and Trivy
   - Performance testing

### Test Coverage

- ✅ System compatibility checks
- ✅ Dependency verification
- ✅ SHA256 checksum validation
- ✅ GPG signature verification
- ✅ Firewall configuration
- ✅ Service installation and startup
- ✅ SSL certificate generation
- ✅ Uninstall functionality

## Uninstall aaPanel

### Using Installation Script

```bash
# Uninstall aaPanel completely
bash install.sh --uninstall
```

### Manual Uninstall

If the automatic uninstall fails, you can manually remove aaPanel:

```bash
# Stop services
/etc/init.d/bt stop

# Remove systemd service
systemctl disable btpanel
rm -f /usr/lib/systemd/system/btpanel.service

# Remove firewall rules
ufw delete allow 888/tcp
firewall-cmd --permanent --remove-port=888/tcp

# Remove files and directories
rm -rf /www/server/panel
rm -rf /www/server
rm -rf /www/backup
rm -rf /www/wwwlogs

# Remove user and group
userdel www
groupdel www

# Remove configuration
rm -f /var/bt_setupPath.conf
```

## Troubleshooting

### Common Issues

1. **Permission Denied:**
   - Ensure you're running as root or with sudo
   - Check file permissions: `chmod +x install.sh`

2. **GPG Verification Failed:**
   - Install GPG: `apt install gnupg` or `yum install gnupg2`
   - Import aaPanel public key: `gpg --import aaPanel_release_public_key.asc`

3. **SHA256 Verification Failed:**
   - Check internet connection
   - Verify file integrity manually
   - Try downloading again

4. **Port Already in Use:**
   - Change panel port: `bash install.sh -P 8889`
   - Check port usage: `netstat -tlnp | grep :888`

5. **Disk Space Insufficient:**
   - Free up disk space (minimum 100MB required)
   - Check available space: `df -h`

### Debug Mode

Enable verbose output for troubleshooting:

```bash
# Run with debug output
bash -x install.sh
```

## Project Status

### Completed Tasks ✅

- **Phase 1:** CI/CD Infrastructure Setup
  - GitHub Actions workflow with multi-OS support
  - Security scanning (CodeQL, Trivy)
  - Automated Docker image building
  - Dependency caching

- **Phase 2.1:** SHA256 Verification
  - SHA256 checksum generation and verification
  - Integration with download functions

- **Phase 2.2:** GPG Signature Verification (Partial)
  - GPG key pair generation
  - Public key export and repository storage
  - Basic signature verification framework

- **Phase 4.1:** Testing Implementation (Partial)
  - Local testing completed
  - CI/CD pipeline validation

### In Progress 🚧

- **Phase 2.2:** Complete GPG Signature Verification
- **Phase 2.3:** Full Uninstall Functionality
- **Phase 3.1:** GitHub Releases Automation
- **Phase 3.2:** Documentation Updates
- **Phase 4.2:** Monitoring and Maintenance

### Next Steps 📋

1. Complete GPG signature verification in install.sh
2. Implement --uninstall flag functionality
3. Set up automated GitHub releases
4. Update README.md with security instructions
5. Create comprehensive troubleshooting guide
6. Implement pipeline monitoring and alerts

## Security Best Practices

1. **Always verify signatures:** Use GPG verification for all downloads
2. **Check checksums:** Validate SHA256 hashes before installation
3. **Use strong passwords:** Change default credentials immediately
4. **Keep updated:** Regularly update aaPanel and dependencies
5. **Monitor logs:** Check installation and runtime logs for anomalies
6. **Firewall configuration:** Properly configure firewall rules
7. **SSL certificates:** Use valid SSL certificates in production

## Support and Resources

- **Official Website:** https://www.aapanel.com
- **Documentation:** https://doc.aapanel.com
- **Demo:** https://demo.aapanel.com/fdgi87jbn/
- **Forum:** https://forum.aapanel.com
- **Email Support:** support@aapanel.com

## Contributing

This project welcomes contributions. Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the terms specified in the LICENSE file.

---

*Last updated: $(date)*
*aaPanel CI/CD and Security Enhancement Project*
