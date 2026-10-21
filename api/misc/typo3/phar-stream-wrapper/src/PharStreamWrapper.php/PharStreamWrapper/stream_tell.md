# PharStreamWrapper::stream_tell()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php`](../_file.md), lines 342–348 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php#L342-L348)
- **Class:** [PharStreamWrapper](../PharStreamWrapper.md)

## Signature

```php
public function stream_tell()
```

## Documentation

```text
@return int
```

## Code

```php
    public function stream_tell()
    {
        return $this->invokeInternalStreamWrapper(
            'ftell',
            $this->internalResource
        );
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · Licensed GPL-2.0-or-later (see LICENSE)._
