# PharInvocationCollection::assertUniqueBaseName()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php`](../_file.md), lines 84–94 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php#L84-L94)
- **Class:** [PharInvocationCollection](../PharInvocationCollection.md)

## Signature

```php
private function assertUniqueBaseName(PharInvocation $invocation, $flags)
```

## Documentation

```text
Asserts that base-name is unique. This disallows having multiple invocations for
same base-name but having different alias names.

@param PharInvocation $invocation
@param int $flags
@return bool
```

## Code

```php
    private function assertUniqueBaseName(PharInvocation $invocation, $flags)
    {
        if (!($flags & static::UNIQUE_BASE_NAME)) {
            return true;
        }
        return $this->findByCallback(
                function (PharInvocation $candidate) use ($invocation) {
                    return $candidate->getBaseName() === $invocation->getBaseName();
                }
            ) === null;
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php) · Licensed GPL-2.0-or-later (see LICENSE)._
