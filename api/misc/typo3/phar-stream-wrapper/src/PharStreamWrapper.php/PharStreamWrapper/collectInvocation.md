# PharStreamWrapper::collectInvocation()

- **Type:** Method
- **File:** [`misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php`](../_file.md), lines 426–446 · [local source](../../../../../../../source/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php#L426-L446)
- **Class:** [PharStreamWrapper](../PharStreamWrapper.md)

## Signature

```php
protected function collectInvocation($path)
```

## Documentation

```text
@param string $path
```

## Code

```php
    protected function collectInvocation($path)
    {
        if (isset($this->invocation)) {
            return;
        }

        $manager = Manager::instance();
        $this->invocation = $manager->resolve($path);
        if ($this->invocation === null) {
            throw new Exception(
                'Expected invocation could not be resolved',
                1556389591
            );
        }
        // confirm, previous interceptor(s) validated invocation
        $this->invocation->confirm();
        $collection = $manager->getCollection();
        if (!$collection->has($this->invocation)) {
            $collection->collect($this->invocation);
        }
    }
```

---
_Drupal 7.103 · [misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php](https://github.com/drupal/drupal/blob/7.103/misc/typo3/phar-stream-wrapper/src/PharStreamWrapper.php) · Licensed GPL-2.0-or-later (see LICENSE)._
