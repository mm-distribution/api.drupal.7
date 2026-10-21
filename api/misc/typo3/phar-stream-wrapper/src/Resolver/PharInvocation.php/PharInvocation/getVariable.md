# PharInvocation::getVariable()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocation.php`](../_file.md), lines 99–105 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocation.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocation.php#L99-L105)
- **Class:** [PharInvocation](../PharInvocation.md)

## Signature

```php
public function getVariable($name)
```

## Documentation

```text
@param string $name
@return mixed|null
```

## Code

```php
    public function getVariable($name)
    {
        if (!isset($this->variables[$name])) {
            return null;
        }
        return $this->variables[$name];
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocation.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocation.php) · Licensed GPL-2.0-or-later (see LICENSE)._
