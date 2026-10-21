# PharInvocationResolver::findByAlias()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php`](../_file.md), lines 236–248 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php#L236-L248)
- **Class:** [PharInvocationResolver](../PharInvocationResolver.md)

## Signature

```php
private function findByAlias($path)
```

## Documentation

```text
Finds confirmed(!) invocations by alias.

@param string $path
@return null|PharInvocation
@see \TYPO3\PharStreamWrapper\PharStreamWrapper::collectInvocation()
```

## Code

```php
    private function findByAlias($path)
    {
        $possibleAlias = $this->resolvePossibleAlias($path);
        if ($possibleAlias === null) {
            return null;
        }
        return Manager::instance()->getCollection()->findByCallback(
            function (PharInvocation $candidate) use ($possibleAlias) {
                return $candidate->isConfirmed() && $candidate->getAlias() === $possibleAlias;
            },
            true
        );
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php) · Licensed GPL-2.0-or-later (see LICENSE)._
