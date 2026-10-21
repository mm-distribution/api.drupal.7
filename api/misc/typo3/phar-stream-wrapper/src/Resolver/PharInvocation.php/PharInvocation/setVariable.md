# PharInvocation::setVariable()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocation.php`](../_file.md), lines 111–114 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocation.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocation.php#L111-L114)
- **Class:** [PharInvocation](../PharInvocation.md)

## Signature

```php
public function setVariable($name, $value)
```

## Documentation

```text
@param string $name
@param mixed $value
```

## Code

```php
    public function setVariable($name, $value)
    {
        $this->variables[$name] = $value;
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocation.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocation.php) · Licensed GPL-2.0-or-later (see LICENSE)._
