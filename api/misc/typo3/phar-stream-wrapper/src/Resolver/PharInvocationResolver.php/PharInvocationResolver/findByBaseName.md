# PharInvocationResolver::findByBaseName()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php`](../_file.md), lines 182–190 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php#L182-L190)
- **Class:** [PharInvocationResolver](../PharInvocationResolver.md)

## Signature

```php
private function findByBaseName($baseName)
```

## Documentation

```text
@param string $baseName
@return null|PharInvocation
```

## Code

```php
    private function findByBaseName($baseName)
    {
        return Manager::instance()->getCollection()->findByCallback(
            function (PharInvocation $candidate) use ($baseName) {
                return $candidate->getBaseName() === $baseName;
            },
            true
        );
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationResolver.php) · Licensed GPL-2.0-or-later (see LICENSE)._
