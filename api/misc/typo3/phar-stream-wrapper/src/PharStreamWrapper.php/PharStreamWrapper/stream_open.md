# PharStreamWrapper::stream_open()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php`](../_file.md), lines 237–265 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php#L237-L265)
- **Class:** [PharStreamWrapper](../PharStreamWrapper.md)

## Signature

```php
public function stream_open(
        $path,
        $mode,
        $options,
        &$opened_path = null
    )
```

## Documentation

```text
@param string $path
@param string $mode
@param int $options
@param string|null $opened_path
@return bool
```

## Code

```php
    public function stream_open(
        $path,
        $mode,
        $options,
        &$opened_path = null
    ) {
        $this->assert($path, Behavior::COMMAND_STREAM_OPEN);
        $arguments = array($path, $mode, (bool) ($options & STREAM_USE_PATH));
        // only add stream context for non include/require calls
        if (!($options & static::STREAM_OPEN_FOR_INCLUDE)) {
            $arguments[] = $this->context;
        // work around https://bugs.php.net/bug.php?id=66569
        // for including files from Phar stream with OPcache enabled
        } else {
            Helper::resetOpCache();
        }
        $this->internalResource = call_user_func_array(
            array($this, 'invokeInternalStreamWrapper'),
            array_merge(array('fopen'), $arguments)
        );
        if (!is_resource($this->internalResource)) {
            return false;
        }
        if ($opened_path !== null) {
            $metaData = stream_get_meta_data($this->internalResource);
            $opened_path = $metaData['uri'];
        }
        return true;
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · Licensed GPL-2.0-or-later (see LICENSE)._
