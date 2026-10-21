# Helper::removePharPrefix()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Helper.php`](../_file.md), lines 77–84 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Helper.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Helper.php#L77-L84)
- **Class:** [Helper](../Helper.md)

## Signature

```php
public static function removePharPrefix($path)
```

## Documentation

```text
@param string $path
@return string
```

## Code

```php
    public static function removePharPrefix($path)
    {
        $path = trim($path);
        if (!static::hasPharPrefix($path)) {
            return $path;
        }
        return substr($path, 7);
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Helper.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Helper.php) · Licensed GPL-2.0-or-later (see LICENSE)._
