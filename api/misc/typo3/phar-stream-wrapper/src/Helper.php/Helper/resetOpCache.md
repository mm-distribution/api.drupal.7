# Helper::resetOpCache()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Helper.php`](../_file.md), lines 29–39 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Helper.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Helper.php#L29-L39)
- **Class:** [Helper](../Helper.md)

## Signature

```php
public static function resetOpCache()
```

## Documentation

_No docblock in source._

## Code

```php
    public static function resetOpCache()
    {
        if (function_exists('opcache_reset')
            && function_exists('opcache_get_status')
        ) {
            $status = opcache_get_status();
            if (!empty($status['opcache_enabled'])) {
                opcache_reset();
            }
        }
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Helper.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Helper.php) · Licensed GPL-2.0-or-later (see LICENSE)._
