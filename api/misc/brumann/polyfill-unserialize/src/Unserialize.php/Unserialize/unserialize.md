# Unserialize::unserialize()

- **Type:** Method
- **File:** [`misc/brumann/polyfill-unserialize/src/Unserialize.php`](../_file.md), lines 15–57 · [local source](../../../../../../../source/misc/brumann/polyfill-unserialize/src/Unserialize.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/misc/brumann/polyfill-unserialize/src/Unserialize.php#L15-L57)
- **Class:** [Unserialize](../Unserialize.md)

## Signature

```php
public static function unserialize($serialized, array $options = array())
```

## Documentation

```text
@see https://secure.php.net/manual/en/function.unserialize.php

@param string $serialized Serialized data
@param array $options Associative array containing options

@return mixed
```

## Code

```php
    public static function unserialize($serialized, array $options = array())
    {
        if (PHP_VERSION_ID >= 70000) {
            return \unserialize($serialized, $options);
        }
        if (!array_key_exists('allowed_classes', $options)) {
            $options['allowed_classes'] = true;
        }
        $allowedClasses = $options['allowed_classes'];
        if (true === $allowedClasses) {
            return \unserialize($serialized);
        }
        if (false === $allowedClasses) {
            $allowedClasses = array();
        }
        if (!is_array($allowedClasses)) {
            trigger_error(
                'unserialize(): allowed_classes option should be array or boolean',
                E_USER_WARNING
            );
            $allowedClasses = array();
        }

        $sanitizedSerialized = preg_replace_callback(
            '/(^|;)O:\d+:"([^"]*)":(\d+):{/',
            function ($match) use ($allowedClasses) {
                list($completeMatch, $leftBorder, $className, $objectSize) = $match;
                if (in_array($className, $allowedClasses)) {
                    return $completeMatch;
                } else {
                    return sprintf(
                        '%sO:22:"__PHP_Incomplete_Class":%d:{s:27:"__PHP_Incomplete_Class_Name";%s',
                        $leftBorder,
                        $objectSize + 1, // size of object + 1 for added string
                        \serialize($className)
                    );
                }
            },
            $serialized
        );

        return \unserialize($sanitizedSerialized);
    }
```

---
_Drupal 7.103 · [misc/brumann/polyfill-unserialize/src/Unserialize.php](https://github.com/drupal/drupal/blob/7.103/misc/brumann/polyfill-unserialize/src/Unserialize.php) · Licensed GPL-2.0-or-later (see LICENSE)._
