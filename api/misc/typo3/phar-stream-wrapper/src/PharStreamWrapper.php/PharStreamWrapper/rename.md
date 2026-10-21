# PharStreamWrapper::rename()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php`](../_file.md), lines 121–131 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php#L121-L131)
- **Class:** [PharStreamWrapper](../PharStreamWrapper.md)

## Signature

```php
public function rename($path_from, $path_to)
```

## Documentation

```text
@param string $path_from
@param string $path_to
@return bool
```

## Code

```php
    public function rename($path_from, $path_to)
    {
        $this->assert($path_from, Behavior::COMMAND_RENAME);
        $this->assert($path_to, Behavior::COMMAND_RENAME);
        return $this->invokeInternalStreamWrapper(
            'rename',
            $path_from,
            $path_to,
            $this->context
        );
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · Licensed GPL-2.0-or-later (see LICENSE)._
