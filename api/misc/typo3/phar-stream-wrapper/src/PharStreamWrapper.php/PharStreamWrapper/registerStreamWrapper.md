# PharStreamWrapper::registerStreamWrapper()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php`](../_file.md), lines 495–499 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php#L495-L499)
- **Class:** [PharStreamWrapper](../PharStreamWrapper.md)

## Signature

```php
private function registerStreamWrapper()
```

## Documentation

_No docblock in source._

## Code

```php
    private function registerStreamWrapper()
    {
        stream_wrapper_unregister('phar');
        stream_wrapper_register('phar', get_class($this));
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · Licensed GPL-2.0-or-later (see LICENSE)._
