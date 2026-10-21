# Manager::destroy()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Manager.php`](../_file.md), lines 78–85 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Manager.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Manager.php#L78-L85)
- **Class:** [Manager](../Manager.md)

## Signature

```php
public static function destroy()
```

## Documentation

```text
@return bool
```

## Code

```php
    public static function destroy()
    {
        if (self::$instance === null) {
            return false;
        }
        self::$instance = null;
        return true;
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Manager.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Manager.php) · Licensed GPL-2.0-or-later (see LICENSE)._
