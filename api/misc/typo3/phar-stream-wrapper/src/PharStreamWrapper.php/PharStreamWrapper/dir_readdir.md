# PharStreamWrapper::dir_readdir()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php`](../_file.md), lines 74–80 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php#L74-L80)
- **Class:** [PharStreamWrapper](../PharStreamWrapper.md)

## Signature

```php
public function dir_readdir()
```

## Documentation

```text
@return string|false
```

## Code

```php
    public function dir_readdir()
    {
        return $this->invokeInternalStreamWrapper(
            'readdir',
            $this->internalResource
        );
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · Licensed GPL-2.0-or-later (see LICENSE)._
