# PharStreamWrapper::stream_flush()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php`](../_file.md), lines 170–176 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php#L170-L176)
- **Class:** [PharStreamWrapper](../PharStreamWrapper.md)

## Signature

```php
public function stream_flush()
```

## Documentation

```text
@return bool
```

## Code

```php
    public function stream_flush()
    {
        return $this->invokeInternalStreamWrapper(
            'fflush',
            $this->internalResource
        );
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · Licensed GPL-2.0-or-later (see LICENSE)._
