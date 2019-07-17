var percentages = range(0, 100, 5).map(s => s + '%')

var t1 = just.timeline();

t1.add({
   targets: ".progress-bar",
   easing: 'ease-in-out',
   duration: 75000,
   props: {
     innerHTML: percentages,
     '--progress': [0, 100]
   }
})

t1.play({
   repeat: Infinity
});

just.tools.player(t1);

function range(start, end, step) {
   const results = []
   for (var x = start; x < end; x = Math.min(end, x + just.random(1, step, null, true))) {
      results.push(x)
   }
   results.push(end)
   return results
}