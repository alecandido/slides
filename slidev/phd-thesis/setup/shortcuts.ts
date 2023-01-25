import type { NavOperations, ShortcutOptions } from '@slidev/types'
import { defineShortcutsSetup } from '@slidev/types'


export default defineShortcutsSetup((nav: NavOperations, base: ShortcutOptions[]) => {
  console.log(base)
  return [
    ...base.filter(
      map => !["goto", "prev_left", "next_right"].includes(map.name)
    ),
    {
      key: 'h',
      fn: () => nav.prev(),
      autoRepeat: true,
    },
    {
      key: 'l',
      fn: () => nav.next(),
      autoRepeat: true,
    },
    {
      key: 'k',
      fn: () => nav.prevSlide(),
      autoRepeat: true,
    },
    {
      key: 'j',
      fn: () => nav.nextSlide(),
      autoRepeat: true,
    },
    {
      key: 'g',
      fn: () => nav.goFirst(),
      autoRepeat: true,
    },
    {
      key: 'shift+g',
      fn: () => nav.goLast(),
      autoRepeat: true,
    },
    {
      key: 't',
      fn: () => nav.showGotoDialog(),
      autoRepeat: true,
    },
    {
      key: 'b',
      fn: () => nav.go(2),
      autoRepeat: true,
    },
    {
      key: 'e',
      fn: () => nav.go(30),
      autoRepeat: true,
    },
    {
      key: 'u',
      fn: () => history.back(),
      autoRepeat: true,
    },
    {
      key: 'r',
      fn: () => history.forward(),
      autoRepeat: true,
    },
  ]
})

