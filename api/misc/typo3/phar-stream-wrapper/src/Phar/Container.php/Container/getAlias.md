# Container::getAlias()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Phar/Container.php`](../_file.md), lines 55–58 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Phar/Container.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Phar/Container.php#L55-L58)
- **Class:** [Container](../Container.md)

## Signature

```php
public function getAlias()
```

## Documentation

```text
@return string
```

## Code

```php
    public function getAlias()
    {
        return $this->manifest->getAlias() ?: $this->stub->getMappedAlias();
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Phar/Container.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Phar/Container.php) · Licensed GPL-2.0-or-later (see LICENSE)._
