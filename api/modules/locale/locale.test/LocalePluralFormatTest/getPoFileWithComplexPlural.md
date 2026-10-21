# LocalePluralFormatTest::getPoFileWithComplexPlural()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 890–909 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L890-L909)
- **Class:** [LocalePluralFormatTest](../LocalePluralFormatTest.md)
- **Module/theme:** locale

## Signature

```php
function getPoFileWithComplexPlural()
```

## Documentation

```text
Returns a .po file with a complex plural formula.
```

## Code

```php
  function getPoFileWithComplexPlural() {
    return <<< EOF
msgid ""
msgstr ""
"Project-Id-Version: Drupal 7\\n"
"MIME-Version: 1.0\\n"
"Content-Type: text/plain; charset=UTF-8\\n"
"Content-Transfer-Encoding: 8bit\\n"
"Plural-Forms: nplurals=3; plural=n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2;\\n"

msgid "1 hour"
msgid_plural "@count hours"
msgstr[0] "@count sat"
msgstr[1] "@count sata"
msgstr[2] "@count sati"

msgid "Monday"
msgstr "Ponedjeljak"
EOF;
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
