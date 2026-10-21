# PharStreamWrapper::stream_metadata()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php`](../_file.md), lines 197–228 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php#L197-L228)
- **Class:** [PharStreamWrapper](../PharStreamWrapper.md)

## Signature

```php
public function stream_metadata($path, $option, $value)
```

## Documentation

```text
@param string $path
@param int $option
@param string|int $value
@return bool
```

## Code

```php
    public function stream_metadata($path, $option, $value)
    {
        $this->assert($path, Behavior::COMMAND_STEAM_METADATA);
        if ($option === STREAM_META_TOUCH) {
            return call_user_func_array(
                array($this, 'invokeInternalStreamWrapper'),
                array_merge(array('touch', $path), (array) $value)
            );
        }
        if ($option === STREAM_META_OWNER_NAME || $option === STREAM_META_OWNER) {
            return $this->invokeInternalStreamWrapper(
                'chown',
                $path,
                $value
            );
        }
        if ($option === STREAM_META_GROUP_NAME || $option === STREAM_META_GROUP) {
            return $this->invokeInternalStreamWrapper(
                'chgrp',
                $path,
                $value
            );
        }
        if ($option === STREAM_META_ACCESS) {
            return $this->invokeInternalStreamWrapper(
                'chmod',
                $path,
                $value
            );
        }
        return false;
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · Licensed GPL-2.0-or-later (see LICENSE)._
