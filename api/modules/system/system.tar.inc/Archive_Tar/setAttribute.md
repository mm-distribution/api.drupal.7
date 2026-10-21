# Archive_Tar::setAttribute()

- **Type:** Method
- **File:** [`modules/system/system.tar.inc`](../_file.md), lines 726–770 · [local source](../../../../../source/modules/system/system.tar.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc#L726-L770)
- **Class:** [Archive_Tar](../Archive_Tar.md)
- **Module/theme:** system

## Signature

```php
public function setAttribute()
```

## Documentation

```text
This method set specific attributes of the archive. It uses a variable
list of parameters, in the format attribute code + attribute values :
$arch->setAttribute(ARCHIVE_TAR_ATT_SEPARATOR, ',');

@return bool true on success, false on error.
```

## Code

```php
    public function setAttribute()
    {
        $v_result = true;

        // ----- Get the number of variable list of arguments
        if (($v_size = func_num_args()) == 0) {
            return true;
        }

        // ----- Get the arguments
        $v_att_list = func_get_args();

        // ----- Read the attributes
        $i = 0;
        while ($i < $v_size) {

            // ----- Look for next option
            switch ($v_att_list[$i]) {
                // ----- Look for options that request a string value
                case ARCHIVE_TAR_ATT_SEPARATOR :
                    // ----- Check the number of parameters
                    if (($i + 1) >= $v_size) {
                        $this->_error(
                            'Invalid number of parameters for '
                            . 'attribute ARCHIVE_TAR_ATT_SEPARATOR'
                        );
                        return false;
                    }

                    // ----- Get the value
                    $this->_separator = $v_att_list[$i + 1];
                    $i++;
                    break;

                default :
                    $this->_error('Unknown attribute code ' . $v_att_list[$i] . '');
                    return false;
            }

            // ----- Next attribute
            $i++;
        }

        return $v_result;
    }
```

---
_Drupal 7.103 · [modules/system/system.tar.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.tar.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
