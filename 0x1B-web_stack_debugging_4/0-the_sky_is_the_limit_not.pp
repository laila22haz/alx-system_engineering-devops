# Adjust ulimit and restart Nginx
exec { 'replace':
  command     => "sed -i 's/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/g' /etc/default/nginx && /usr/sbin/service nginx restart",
  path        => ['/bin', '/usr/bin', '/usr/sbin'],
}
