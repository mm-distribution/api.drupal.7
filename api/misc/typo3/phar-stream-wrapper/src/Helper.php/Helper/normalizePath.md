# Helper::normalizePath()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Helper.php`](../_file.md), lines 93–101 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Helper.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Helper.php#L93-L101)
- **Class:** [Helper](../Helper.md)

## Signature

```php
public static function normalizePath($path)
```

## Documentation

```text
Normalizes a path, removes phar:// prefix, fixes Windows directory
separators. Result is without trailing slash.

@param string $path
@return string
```

## Code

```php
    public static function normalizePath($path)
    {
        return rtrim(
            static::normalizeWindowsPath(
                static::removePharPrefix($path)
            ),
            '/'
        );
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Helper.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Helper.php) · Licensed GPL-2.0-or-later (see LICENSE)._
