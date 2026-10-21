# Manager::__construct()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Manager.php`](../_file.md), lines 92–106 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Manager.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Manager.php#L92-L106)
- **Class:** [Manager](../Manager.md)

## Signature

```php
private function __construct(
        Behavior $behaviour,
        Resolvable $resolver = null,
        Collectable $collection = null
    )
```

## Documentation

```text
@param Behavior $behaviour
@param Resolvable $resolver
@param Collectable $collection
```

## Code

```php
    private function __construct(
        Behavior $behaviour,
        Resolvable $resolver = null,
        Collectable $collection = null
    ) {
        if ($collection === null) {
            $collection = new PharInvocationCollection();
        }
        if ($resolver === null) {
            $resolver = new PharInvocationResolver();
        }
        $this->collection = $collection;
        $this->resolver = $resolver;
        $this->behavior = $behaviour;
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Manager.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Manager.php) · Licensed GPL-2.0-or-later (see LICENSE)._
