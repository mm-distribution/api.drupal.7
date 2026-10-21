# file_htaccess_lines()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 525–567 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L525-L567)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_htaccess_lines($private = TRUE)
```

## Documentation

```text
Returns the standard .htaccess lines that Drupal writes to file directories.

@param $private
  (Optional) Set to FALSE to return the .htaccess lines for an open and
  public directory. The default is TRUE, which returns the .htaccess lines
  for a private and protected directory.

@return
  A string representing the desired contents of the .htaccess file.

@see file_create_htaccess()
```

## Code

```php
function file_htaccess_lines($private = TRUE) {
  $lines = <<<EOF
# Turn off all options we don't need.
Options None
Options +FollowSymLinks

# Set the catch-all handler to prevent scripts from being executed.
SetHandler Drupal_Security_Do_Not_Remove_See_SA_2006_006
<Files *>
  # Override the handler again if we're run later in the evaluation list.
  SetHandler Drupal_Security_Do_Not_Remove_See_SA_2013_003
</Files>

# If we know how to do it safely, disable the PHP engine entirely.
<IfModule mod_php5.c>
  php_flag engine off
</IfModule>
<IfModule mod_php7.c>
  php_flag engine off
</IfModule>
# From PHP 8 there is no number in the module name.
<IfModule mod_php.c>
  php_flag engine off
</IfModule>
EOF;

  if ($private) {
    $lines = <<<EOF
# Deny all requests from Apache 2.4+.
<IfModule mod_authz_core.c>
  Require all denied
</IfModule>

# Deny all requests from Apache 2.0-2.2.
<IfModule !mod_authz_core.c>
  Deny from all
</IfModule>
EOF
    . "\n\n" . $lines;
  }

  return $lines;
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
