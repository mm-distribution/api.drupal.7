# PharInvocation::equals()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocation.php`](../_file.md), lines 120–124 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocation.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocation.php#L120-L124)
- **Class:** [PharInvocation](../PharInvocation.md)

## Signature

```php
public function equals(PharInvocation $other)
```

## Documentation

```text
@param PharInvocation $other
@return bool
```

## Code

```php
    public function equals(PharInvocation $other)
    {
        return $other->baseName === $this->baseName
            && $other->alias === $this->alias;
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocation.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocation.php) · Licensed GPL-2.0-or-later (see LICENSE)._
