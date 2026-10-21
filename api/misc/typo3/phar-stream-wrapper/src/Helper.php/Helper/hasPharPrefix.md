# Helper::hasPharPrefix()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Helper.php`](../_file.md), lines 68–71 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Helper.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Helper.php#L68-L71)
- **Class:** [Helper](../Helper.md)

## Signature

```php
public static function hasPharPrefix($path)
```

## Documentation

```text
@param string $path
@return bool
```

## Code

```php
    public static function hasPharPrefix($path)
    {
        return stripos($path, 'phar://') === 0;
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Helper.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Helper.php) · Licensed GPL-2.0-or-later (see LICENSE)._
