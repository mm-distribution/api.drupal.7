# PharInvocationCollection::triggerDuplicateAliasWarning()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php`](../_file.md), lines 122–143 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php#L122-L143)
- **Class:** [PharInvocationCollection](../PharInvocationCollection.md)

## Signature

```php
private function triggerDuplicateAliasWarning(PharInvocation $invocation)
```

## Documentation

```text
Triggers warning for invocations with same alias and same confirmation state.

@param PharInvocation $invocation
@see \TYPO3\PharStreamWrapper\PharStreamWrapper::collectInvocation()
```

## Code

```php
    private function triggerDuplicateAliasWarning(PharInvocation $invocation)
    {
        $sameAliasInvocation = $this->findByCallback(
            function (PharInvocation $candidate) use ($invocation) {
                return $candidate->isConfirmed() === $invocation->isConfirmed()
                    && $candidate->getAlias() === $invocation->getAlias();
            },
            true
        );
        if ($sameAliasInvocation === null) {
            return;
        }
        trigger_error(
            sprintf(
                'Alias %s cannot be used by %s, already used by %s',
                $invocation->getAlias(),
                $invocation->getBaseName(),
                $sameAliasInvocation->getBaseName()
            ),
            E_USER_WARNING
        );
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php) · Licensed GPL-2.0-or-later (see LICENSE)._
