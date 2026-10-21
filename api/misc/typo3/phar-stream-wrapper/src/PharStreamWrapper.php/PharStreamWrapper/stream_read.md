# PharStreamWrapper::stream_read()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php`](../_file.md), lines 271–278 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php#L271-L278)
- **Class:** [PharStreamWrapper](../PharStreamWrapper.md)

## Signature

```php
public function stream_read($count)
```

## Documentation

```text
@param int $count
@return string
```

## Code

```php
    public function stream_read($count)
    {
        return $this->invokeInternalStreamWrapper(
            'fread',
            $this->internalResource,
            $count
        );
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · Licensed GPL-2.0-or-later (see LICENSE)._
