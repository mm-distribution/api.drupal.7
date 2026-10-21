# PharInvocationCollection::findByCallback()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php`](../_file.md), lines 66–74 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php#L66-L74)
- **Class:** [PharInvocationCollection](../PharInvocationCollection.md)

## Signature

```php
public function findByCallback($callback, $reverse = false)
```

## Documentation

```text
@param callable $callback
@param bool $reverse
@return null|PharInvocation
```

## Code

```php
    public function findByCallback($callback, $reverse = false)
    {
        foreach ($this->getInvocations($reverse) as $invocation) {
            if (call_user_func($callback, $invocation) === true) {
                return $invocation;
            }
        }
        return null;
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php) · Licensed GPL-2.0-or-later (see LICENSE)._
