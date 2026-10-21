# PharStreamWrapper::stream_eof()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php`](../_file.md), lines 159–165 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php#L159-L165)
- **Class:** [PharStreamWrapper](../PharStreamWrapper.md)

## Signature

```php
public function stream_eof()
```

## Documentation

```text
@return bool
```

## Code

```php
    public function stream_eof()
    {
        return $this->invokeInternalStreamWrapper(
            'feof',
            $this->internalResource
        );
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · Licensed GPL-2.0-or-later (see LICENSE)._
