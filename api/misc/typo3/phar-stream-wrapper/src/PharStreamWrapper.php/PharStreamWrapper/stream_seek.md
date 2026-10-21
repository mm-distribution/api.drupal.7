# PharStreamWrapper::stream_seek()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php`](../_file.md), lines 285–293 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php#L285-L293)
- **Class:** [PharStreamWrapper](../PharStreamWrapper.md)

## Signature

```php
public function stream_seek($offset, $whence = SEEK_SET)
```

## Documentation

```text
@param int $offset
@param int $whence
@return bool
```

## Code

```php
    public function stream_seek($offset, $whence = SEEK_SET)
    {
        return $this->invokeInternalStreamWrapper(
            'fseek',
            $this->internalResource,
            $offset,
            $whence
        ) !== -1;
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · Licensed GPL-2.0-or-later (see LICENSE)._
