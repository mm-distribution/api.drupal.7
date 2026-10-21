# PharStreamWrapper::unlink()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php`](../_file.md), lines 380–388 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php#L380-L388)
- **Class:** [PharStreamWrapper](../PharStreamWrapper.md)

## Signature

```php
public function unlink($path)
```

## Documentation

```text
@param string $path
@return bool
```

## Code

```php
    public function unlink($path)
    {
        $this->assert($path, Behavior::COMMAND_UNLINK);
        return $this->invokeInternalStreamWrapper(
            'unlink',
            $path,
            $this->context
        );
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · Licensed GPL-2.0-or-later (see LICENSE)._
