# Helper::isAbsolutePath()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Helper.php`](../_file.md), lines 181–190 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Helper.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Helper.php#L181-L190)
- **Class:** [Helper](../Helper.md)

## Signature

```php
private static function isAbsolutePath($path)
```

## Documentation

```text
Checks if the $path is absolute or relative (detecting either '/' or
'x:/' as first part of string) and returns TRUE if so.

@param string $path File path to evaluate
@return bool
```

## Code

```php
    private static function isAbsolutePath($path)
    {
        // Path starting with a / is always absolute, on every system
        // On Windows also a path starting with a drive letter is absolute: X:/
        return (isset($path[0]) ? $path[0] : null) === '/'
            || static::isWindows() && (
                strpos($path, ':/') === 1
                || strpos($path, ':\\') === 1
            );
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Helper.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Helper.php) · Licensed GPL-2.0-or-later (see LICENSE)._
