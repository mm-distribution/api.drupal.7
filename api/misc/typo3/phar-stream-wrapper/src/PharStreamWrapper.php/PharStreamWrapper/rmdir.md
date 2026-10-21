# PharStreamWrapper::rmdir()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php`](../_file.md), lines 138–146 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php#L138-L146)
- **Class:** [PharStreamWrapper](../PharStreamWrapper.md)

## Signature

```php
public function rmdir($path, $options)
```

## Documentation

```text
@param string $path
@param int $options
@return bool
```

## Code

```php
    public function rmdir($path, $options)
    {
        $this->assert($path, Behavior::COMMAND_RMDIR);
        return $this->invokeInternalStreamWrapper(
            'rmdir',
            $path,
            $this->context
        );
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · Licensed GPL-2.0-or-later (see LICENSE)._
