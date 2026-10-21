# PharStreamWrapper::stream_set_option()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php`](../_file.md), lines 301–326 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php#L301-L326)
- **Class:** [PharStreamWrapper](../PharStreamWrapper.md)

## Signature

```php
public function stream_set_option($option, $arg1, $arg2)
```

## Documentation

```text
@param int $option
@param int $arg1
@param int $arg2
@return bool
```

## Code

```php
    public function stream_set_option($option, $arg1, $arg2)
    {
        if ($option === STREAM_OPTION_BLOCKING) {
            return $this->invokeInternalStreamWrapper(
                'stream_set_blocking',
                $this->internalResource,
                $arg1
            );
        }
        if ($option === STREAM_OPTION_READ_TIMEOUT) {
            return $this->invokeInternalStreamWrapper(
                'stream_set_timeout',
                $this->internalResource,
                $arg1,
                $arg2
            );
        }
        if ($option === STREAM_OPTION_WRITE_BUFFER) {
            return $this->invokeInternalStreamWrapper(
                'stream_set_write_buffer',
                $this->internalResource,
                $arg2
            ) === 0;
        }
        return false;
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · Licensed GPL-2.0-or-later (see LICENSE)._
