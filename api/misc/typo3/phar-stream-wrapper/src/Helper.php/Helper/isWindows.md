# Helper::isWindows()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Helper.php`](../_file.md), lines 195–198 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Helper.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Helper.php#L195-L198)
- **Class:** [Helper](../Helper.md)

## Signature

```php
private static function isWindows()
```

## Documentation

```text
@return bool
```

## Code

```php
    private static function isWindows()
    {
        return stripos(PHP_OS, 'WIN') === 0;
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Helper.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Helper.php) · Licensed GPL-2.0-or-later (see LICENSE)._
