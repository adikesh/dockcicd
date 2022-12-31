FROM httpd
copy waste.py /usr/local/apache2/htdocs
EXPOSE 443
