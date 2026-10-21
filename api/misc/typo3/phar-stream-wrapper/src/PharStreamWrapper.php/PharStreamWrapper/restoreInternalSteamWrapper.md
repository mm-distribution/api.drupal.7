# PharStreamWrapper::restoreInternalSteamWrapper()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php`](../_file.md), lines 490–493 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php#L490-L493)
- **Class:** [PharStreamWrapper](../PharStreamWrapper.md)

## Signature

```php
private function restoreInternalSteamWrapper()
```

## Documentation

_No docblock in source._

## Code

```php
    private function restoreInternalSteamWrapper()
    {
        stream_wrapper_restore('phar');
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · Licensed GPL-2.0-or-later (see LICENSE)._
