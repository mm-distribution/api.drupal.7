# PharStreamWrapper::dir_opendir()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php`](../_file.md), lines 60–69 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php#L60-L69)
- **Class:** [PharStreamWrapper](../PharStreamWrapper.md)

## Signature

```php
public function dir_opendir($path, $options)
```

## Documentation

```text
@param string $path
@param int $options
@return bool
```

## Code

```php
    public function dir_opendir($path, $options)
    {
        $this->assert($path, Behavior::COMMAND_DIR_OPENDIR);
        $this->internalResource = $this->invokeInternalStreamWrapper(
            'opendir',
            $path,
            $this->context
        );
        return is_resource($this->internalResource);
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · Licensed GPL-2.0-or-later (see LICENSE)._
