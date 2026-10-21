# PharInvocationCollection::assertUniqueInvocation()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php`](../_file.md), lines 104–114 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php#L104-L114)
- **Class:** [PharInvocationCollection](../PharInvocationCollection.md)

## Signature

```php
private function assertUniqueInvocation(PharInvocation $invocation, $flags)
```

## Documentation

```text
Asserts that combination of base-name and alias is unique. This allows having multiple
invocations for same base-name but having different alias names (for whatever reason).

@param PharInvocation $invocation
@param int $flags
@return bool
```

## Code

```php
    private function assertUniqueInvocation(PharInvocation $invocation, $flags)
    {
        if (!($flags & static::UNIQUE_INVOCATION)) {
            return true;
        }
        return $this->findByCallback(
                function (PharInvocation $candidate) use ($invocation) {
                    return $candidate->equals($invocation);
                }
            ) === null;
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php) · Licensed GPL-2.0-or-later (see LICENSE)._
