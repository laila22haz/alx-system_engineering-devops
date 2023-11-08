# replace the extension .phpp with .php in wp-settings.php

file { '/var/www/html/wp-includes/class-wp-locale.php':
  ensure  => file,
  source  => '/var/www/html/wp-includes/class-wp-locale.phpp',
  replace => false, # To replace content, set this to 'true' (it may have some limitations)
}

exec { 'fix_wp_locale':
  command => 'sed -i "s/.phpp/.php/g" /var/www/html/wp-includes/class-wp-locale.php',
}
