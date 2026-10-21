# Archive_Tar::loadExtension()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 296–323 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L296-L323)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public static function loadExtension($ext)
```

## Documentation

```text
OS independent PHP extension load. Remember to take care
on the correct extension name for case sensitive OSes.

@param string $ext The extension name
@return bool Success or not on the dl() call
```

## Code

```php
    public static function loadExtension($ext)
    {
        if (extension_loaded($ext)) {
            return true;
        }

        // if either returns true dl() will produce a FATAL error, stop that
        if (
            function_exists('dl') === false ||
            ini_get('enable_dl') != 1
        ) {
            return false;
        }

        if (OS_WINDOWS) {
            $suffix = '.dll';
        } elseif (PHP_OS == 'HP-UX') {
            $suffix = '.sl';
        } elseif (PHP_OS == 'AIX') {
            $suffix = '.a';
        } elseif (PHP_OS == 'OSX') {
            $suffix = '.bundle';
        } else {
            $suffix = '.so';
        }

        return @dl('php_'.$ext.$suffix) || @dl($ext.$suffix);
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
