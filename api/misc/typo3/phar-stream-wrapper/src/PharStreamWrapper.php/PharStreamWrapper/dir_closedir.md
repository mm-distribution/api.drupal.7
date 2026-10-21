# PharStreamWrapper::dir_closedir()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php`](../_file.md), lines 42–53 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php#L42-L53)
- **Class:** [PharStreamWrapper](../PharStreamWrapper.md)

## Signature

```php
public function dir_closedir()
```

## Documentation

```text
@return bool
```

## Code

```php
    public function dir_closedir()
    {
        if (!is_resource($this->internalResource)) {
            return false;
        }

        $this->invokeInternalStreamWrapper(
            'closedir',
            $this->internalResource
        );
        return !is_resource($this->internalResource);
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · Licensed GPL-2.0-or-later (see LICENSE)._
