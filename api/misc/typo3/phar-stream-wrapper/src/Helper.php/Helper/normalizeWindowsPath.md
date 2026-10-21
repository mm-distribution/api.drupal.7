# Helper::normalizeWindowsPath()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Helper.php`](../_file.md), lines 109–112 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Helper.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Helper.php#L109-L112)
- **Class:** [Helper](../Helper.md)

## Signature

```php
public static function normalizeWindowsPath($path)
```

## Documentation

```text
Fixes a path for windows-backslashes and reduces double-slashes to single slashes

@param string $path File path to process
@return string
```

## Code

```php
    public static function normalizeWindowsPath($path)
    {
        return str_replace('\\', '/', $path);
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Helper.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Helper.php) · Licensed GPL-2.0-or-later (see LICENSE)._
