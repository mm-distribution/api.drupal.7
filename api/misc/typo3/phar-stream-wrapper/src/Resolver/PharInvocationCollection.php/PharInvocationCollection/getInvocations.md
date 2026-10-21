# PharInvocationCollection::getInvocations()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php`](../_file.md), lines 149–155 · [local source](../../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php#L149-L155)
- **Class:** [PharInvocationCollection](../PharInvocationCollection.md)

## Signature

```php
private function getInvocations($reverse = false)
```

## Documentation

```text
@param bool $reverse
@return PharInvocation[]
```

## Code

```php
    private function getInvocations($reverse = false)
    {
        if ($reverse) {
            return array_reverse($this->invocations);
        }
        return $this->invocations;
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Resolver/PharInvocationCollection.php) · Licensed GPL-2.0-or-later (see LICENSE)._
