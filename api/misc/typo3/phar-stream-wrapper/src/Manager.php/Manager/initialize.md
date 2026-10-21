# Manager::initialize()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/Manager.php`](../_file.md), lines 46–59 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/Manager.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Manager.php#L46-L59)
- **Class:** [Manager](../Manager.md)

## Signature

```php
public static function initialize(
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
@return self
```

## Code

```php
    public static function initialize(
        Behavior $behaviour,
        Resolvable $resolver = null,
        Collectable $collection = null
    ) {
        if (self::$instance === null) {
            self::$instance = new self($behaviour, $resolver, $collection);
            return self::$instance;
        }
        throw new \LogicException(
            'Manager can only be initialized once',
            1535189871
        );
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/Manager.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/Manager.php) · Licensed GPL-2.0-or-later (see LICENSE)._
