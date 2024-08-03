# Localhost Website Deployment with Nginx and Custom DNS

This guide will walk you through the process of deploying a simple HTML website on your local machine using Nginx, with a custom DNS name 'awesomeweb'.

## Requirements

- Ubuntu or a similar Linux-based operating system.
- Root or sudo privileges.

## Instructions

### 1. Install Nginx

Update your package list and install Nginx:

```bash
sudo apt update
sudo apt install nginx
```

### 2. Set Up Your Website Directory

Create a directory for your website files:

```bash
sudo mkdir -p /var/www/awesomeweb
```

### 3. Create an HTML File

Create an `index.html` file in the directory you just made:

```bash
sudo nano /var/www/awesomeweb/index.html
```

Insert the following HTML code: (Below HTML code is an example for simple HTML file)

```html
<!DOCTYPE html>
<html>
<head>
        <title>Awesome Web</title>
</head>
<body>
        <h1>Welcome to Awesome Web!</h1>
        <p>This is a simple HTML page deployed on Nginx.</p>
        <p>Written By Shubham Rajak</p>
</body>
</html>
```

Save and close the file.

### 4. Adjust Permissions

Set appropriate permissions for the website directory and its contents:

```bash
sudo chmod -R 755 /var/www/awesomeweb
sudo chown -R www-data:www-data /var/www/awesomeweb
```

### 5. Configure Nginx

Create a new Nginx configuration file for your website:

```bash
sudo nano /etc/nginx/sites-available/awesomeweb
```

Add the following configuration:

```nginx
server {
    listen 80;
    server_name awesomeweb;
    root /var/www/awesomeweb;

    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

Save and close the file.

### 6. Enable the Site

Create a symbolic link to enable your site configuration:

```bash
sudo ln -s /etc/nginx/sites-available/awesomeweb /etc/nginx/sites-enabled/
```

### 7. Test Nginx Configuration

Check the Nginx configuration for any syntax errors:

```bash
sudo nginx -t
```

You should see a message indicating the configuration is okay.

### 8. Restart Nginx

Apply the changes by restarting Nginx:

```bash
sudo systemctl restart nginx
```

### 9. Edit the Hosts File

Update your hosts file to map 'awesomeweb' to your localhost:

```bash
sudo nano /etc/hosts
```

Add the following line:

```plaintext
127.0.0.1 awesomeweb
```

Save and close the file.

### 10. Access Your Website

Open your web browser and navigate to:

```
http://awesomeweb
```

You should see the "Welcome to Awesome Web!" page.

## Troubleshooting

### Common Problems

- **404 Not Found**: Check that the document root is correctly set and that permissions are properly configured. Ensure that `index.html` exists in `/var/www/awesomeweb`.
- **Nginx Fails to Start**: Verify there are no syntax errors by running `sudo nginx -t` and check the error log for more details (`sudo tail -f /var/log/nginx/error.log`).

### Log Files

- Error log: `/var/log/nginx/error.log`
- Access log: `/var/log/nginx/access.log`

## Conclusion

You have successfully deployed a simple HTML website on localhost using Nginx with a custom DNS name 'awesomeweb'. This setup can be modified and expanded as needed for more complex use cases.
