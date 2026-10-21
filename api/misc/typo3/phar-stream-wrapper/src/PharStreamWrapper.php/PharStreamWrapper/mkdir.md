# PharStreamWrapper::mkdir()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php`](../_file.md), lines 104–114 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php#L104-L114)
- **Class:** [PharStreamWrapper](../PharStreamWrapper.md)

## Signature

```php
public function mkdir($path, $mode, $options)
```

## Documentation

```text
@param string $path
@param int $mode
@param int $options
@return bool
```

## Code

```php
    public function mkdir($path, $mode, $options)
    {
        $this->assert($path, Behavior::COMMAND_MKDIR);
        return $this->invokeInternalStreamWrapper(
            'mkdir',
            $path,
            $mode,
            (bool) ($options & STREAM_MKDIR_RECURSIVE),
            $this->context
        );
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · Licensed GPL-2.0-or-later (see LICENSE)._
