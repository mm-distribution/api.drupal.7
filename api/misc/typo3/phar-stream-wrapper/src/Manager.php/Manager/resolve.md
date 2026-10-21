# Manager::resolve()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Manager.php`](../_file.md), lines 123–126 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Manager.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Manager.php#L123-L126)
- **Class:** [Manager](../Manager.md)

## Signature

```php
public function resolve($path, $flags = null)
```

## Documentation

```text
@param string $path
@param null|int $flags
@return null|PharInvocation
```

## Code

```php
    public function resolve($path, $flags = null)
    {
        return $this->resolver->resolve($path, $flags);
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Manager.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Manager.php) · Licensed GPL-2.0-or-later (see LICENSE)._
