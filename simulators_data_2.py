# Simulators 5 to 8

SIMULATORS_2 = {
    "sim_05": """
    <div class="eco-card p-6 border-emerald-800/60">
      <div class="flex items-center justify-between mb-4 pb-3 border-b border-emerald-900/60">
        <div>
          <h3 class="text-lg font-bold text-emerald-400">⚠️ Toxic Chemical Plume & Exposure Hazard Calculator</h3>
          <p class="text-xs text-slate-300">Model atmospheric downwind gas dispersion (Bhopal MIC scenario) using the Gaussian Plume Model.</p>
        </div>
        <span class="badge-amber px-2.5 py-1 rounded text-xs font-mono font-bold">Industrial Hazard</span>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
        <div>
          <label class="block text-xs text-slate-300 font-semibold mb-1">Release Rate Q (kg/s): <span id="val_q" class="text-amber-400 font-bold">120</span></label>
          <input type="range" id="input_q" min="10" max="300" value="120" class="w-full accent-amber-500" oninput="runSim05()">
        </div>
        <div>
          <label class="block text-xs text-slate-300 font-semibold mb-1">Wind Velocity u (m/s): <span id="val_u" class="text-cyan-400 font-bold">2.0</span></label>
          <input type="range" id="input_u" min="1.0" max="8.0" step="0.5" value="2.0" class="w-full accent-cyan-500" oninput="runSim05()">
        </div>
        <div>
          <label class="block text-xs text-slate-300 font-semibold mb-1">Atmospheric Stability Class: <span id="val_stab" class="text-emerald-400 font-bold">Class F (Night Inversion)</span></label>
          <select id="input_stab" class="w-full bg-[#06110d] border border-emerald-800 text-xs text-emerald-300 rounded p-1.5" onchange="runSim05()">
            <option value="F" selected>Class F (Stable / Night Inversion - Bhopal Night)</option>
            <option value="D">Class D (Neutral / Overcast)</option>
            <option value="B">Class B (Unstable / Daytime Sun)</option>
          </select>
        </div>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-4">
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-4 text-center">
          <div class="text-xs text-slate-400 uppercase">Concentration at 1 km Downwind</div>
          <div id="out_c1km" class="text-2xl font-black text-red-400 my-1">42.5 ppm</div>
          <div class="text-xs text-red-300 font-bold">Lethal (LC₅₀: 5 ppm)</div>
        </div>
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-4 text-center">
          <div class="text-xs text-slate-400 uppercase">Lethal Hazard Radius (LC₅₀)</div>
          <div id="out_radius" class="text-2xl font-black text-amber-400 my-1">4.2 km</div>
          <div class="text-xs text-slate-400">Severe pulmonary edema zone</div>
        </div>
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-4 text-center">
          <div class="text-xs text-slate-400 uppercase">Emergency Safety Zone Required</div>
          <div id="out_safety" class="text-2xl font-black text-emerald-400 my-1">8.5 km</div>
          <div class="text-xs text-slate-400">IDLH threshold (&lt;0.02 ppm)</div>
        </div>
      </div>
    </div>
    <script>
      function runSim05() {
        const Q = parseFloat(document.getElementById('input_q').value);
        const u = parseFloat(document.getElementById('input_u').value);
        const stab = document.getElementById('input_stab').value;
        document.getElementById('val_q').innerText = Q;
        document.getElementById('val_u').innerText = u.toFixed(1);

        let coeff = 1.0;
        if (stab === 'F') coeff = 2.8;
        else if (stab === 'D') coeff = 1.2;
        else coeff = 0.5;

        const c1km = (Q * coeff * 1.5 / u).toFixed(1);
        const radius = Math.min(15.0, (Math.sqrt(Q * coeff) / u * 1.8)).toFixed(1);
        const safety = (radius * 2.1).toFixed(1);

        document.getElementById('out_c1km').innerText = c1km + ' ppm';
        document.getElementById('out_radius').innerText = radius + ' km';
        document.getElementById('out_safety').innerText = safety + ' km';
      }
      setTimeout(runSim05, 100);
    </script>
    """,

    "06": """
    <div class="eco-card p-6 border-emerald-800/60">
      <div class="flex items-center justify-between mb-4 pb-3 border-b border-emerald-900/60">
        <div>
          <h3 class="text-lg font-bold text-emerald-400">🔄 Biogeochemical Flux & Nutrient Homeostasis Model</h3>
          <p class="text-xs text-slate-300">Simulate perturbations to natural Carbon and Nitrogen cycles through fertilizer synthesis and fossil combustion.</p>
        </div>
        <span class="badge-emerald px-2.5 py-1 rounded text-xs font-mono font-bold">Biogeochemical</span>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
        <div>
          <label class="block text-xs text-slate-300 font-semibold mb-1">Industrial Nitrogen Fixation (Haber-Bosch, Tg N/yr): <span id="val_nfix" class="text-emerald-400 font-bold">140</span></label>
          <input type="range" id="input_nfix" min="50" max="250" value="140" class="w-full accent-emerald-500" oninput="runSim06()">
        </div>
        <div>
          <label class="block text-xs text-slate-300 font-semibold mb-1">Fossil Fuel Carbon Flux (Gt C/yr): <span id="val_cflux" class="text-amber-400 font-bold">9.5</span></label>
          <input type="range" id="input_cflux" min="2.0" max="18.0" step="0.5" value="9.5" class="w-full accent-amber-500" oninput="runSim06()">
        </div>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-4">
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-4 text-center">
          <div class="text-xs text-slate-400 uppercase">Anthropogenic vs Natural N-Fixation</div>
          <div id="out_nratio" class="text-2xl font-black text-emerald-400 my-1">127%</div>
          <div class="text-xs text-slate-400">Doubled planetary baseline</div>
        </div>
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-4 text-center">
          <div class="text-xs text-slate-400 uppercase">Atmospheric CO₂ Growth Rate</div>
          <div id="out_co2_growth" class="text-2xl font-black text-amber-400 my-1">+2.4 ppm/yr</div>
          <div class="text-xs text-slate-400">Ocean/Land airborne fraction ~46%</div>
        </div>
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-4 text-center">
          <div class="text-xs text-slate-400 uppercase">Coastal Eutrophication Dead Zone Index</div>
          <div id="out_deadzone" class="text-2xl font-black text-red-400 my-1">Severe (Index 7.8/10)</div>
          <div class="text-xs text-slate-400">Nutrient runoff to estuaries</div>
        </div>
      </div>
    </div>
    <script>
      function runSim06() {
        const n = parseFloat(document.getElementById('input_nfix').value);
        const c = parseFloat(document.getElementById('input_cflux').value);
        document.getElementById('val_nfix').innerText = n;
        document.getElementById('val_cflux').innerText = c.toFixed(1);

        const natural_N = 110.0;
        const n_ratio = Math.round((n / natural_N) * 100);
        const co2_growth = (c * 0.46 * 0.47).toFixed(2);
        const dz = Math.min(10.0, (n / 250) * 10).toFixed(1);

        document.getElementById('out_nratio').innerText = n_ratio + '% of Natural';
        document.getElementById('out_co2_growth').innerText = '+' + co2_growth + ' ppm/yr';
        document.getElementById('out_deadzone').innerText = (dz > 7.0 ? 'Severe' : 'Moderate') + ' (Index ' + dz + '/10)';
      }
      setTimeout(runSim06, 100);
    </script>
    """,

    "07": """
    <div class="eco-card p-6 border-emerald-800/60">
      <div class="flex items-center justify-between mb-4 pb-3 border-b border-emerald-900/60">
        <div>
          <h3 class="text-lg font-bold text-emerald-400">🌡️ Sea Level Rise & Thermal Expansion Model</h3>
          <p class="text-xs text-slate-300">Calculate global mean sea level rise driven by steric ocean warming and continental ice sheet mass discharge.</p>
        </div>
        <span class="badge-emerald px-2.5 py-1 rounded text-xs font-mono font-bold">Climate Impact</span>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
        <div>
          <label class="block text-xs text-slate-300 font-semibold mb-1">Ocean Temperature Anomaly ΔT (°C): <span id="val_otemp" class="text-cyan-400 font-bold">+0.8 °C</span></label>
          <input type="range" id="input_otemp" min="0.2" max="2.5" step="0.1" value="0.8" class="w-full accent-cyan-500" oninput="runSim07()">
        </div>
        <div>
          <label class="block text-xs text-slate-300 font-semibold mb-1">Polar Ice Sheet Melt (Greenland + Antarctic Gt/yr): <span id="val_imelt" class="text-emerald-400 font-bold">420 Gt/yr</span></label>
          <input type="range" id="input_imelt" min="100" max="1200" step="20" value="420" class="w-full accent-emerald-500" oninput="runSim07()">
        </div>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-4">
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-4 text-center">
          <div class="text-xs text-slate-400 uppercase">Thermosteric Rise (Thermal Expansion)</div>
          <div id="out_thermo" class="text-2xl font-black text-cyan-400 my-1">18.4 cm</div>
          <div class="text-xs text-slate-400">ΔV = V₀ · β · ΔT</div>
        </div>
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-4 text-center">
          <div class="text-xs text-slate-400 uppercase">Cryospheric Mass Addition</div>
          <div id="out_ice" class="text-2xl font-black text-emerald-400 my-1">11.6 cm</div>
          <div class="text-xs text-slate-400">360 Gt = 1 mm sea level</div>
        </div>
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-4 text-center">
          <div class="text-xs text-slate-400 uppercase">Total Sea Level Rise by 2100</div>
          <div id="out_total_slr" class="text-3xl font-black text-amber-400 my-1">30.0 cm</div>
          <div class="text-xs text-slate-400">Excludes storm surges</div>
        </div>
      </div>
    </div>
    <script>
      function runSim07() {
        const oT = parseFloat(document.getElementById('input_otemp').value);
        const iM = parseFloat(document.getElementById('input_imelt').value);
        document.getElementById('val_otemp').innerText = '+' + oT.toFixed(1) + ' °C';
        document.getElementById('val_imelt').innerText = iM + ' Gt/yr';

        const thermosteric = oT * 23.0; // cm
        const ice_cm = (iM / 360.0) * 10; // 100 yr equivalent in cm
        const total = thermosteric + ice_cm;

        document.getElementById('out_thermo').innerText = thermosteric.toFixed(1) + ' cm';
        document.getElementById('out_ice').innerText = ice_cm.toFixed(1) + ' cm';
        document.getElementById('out_total_slr').innerText = total.toFixed(1) + ' cm';
      }
      setTimeout(runSim07, 100);
    </script>
    """,

    "08": """
    <div class="eco-card p-6 border-emerald-800/60">
      <div class="flex items-center justify-between mb-4 pb-3 border-b border-emerald-900/60">
        <div>
          <h3 class="text-lg font-bold text-emerald-400">⚡ AMOC & Climate Tipping Element Hysteresis Explorer</h3>
          <p class="text-xs text-slate-300">Simulate Stommel's two-box model of thermohaline circulation and discover saddle-node bifurcation tipping points.</p>
        </div>
        <span class="badge-amber px-2.5 py-1 rounded text-xs font-mono font-bold">Non-Linear Dynamics</span>
      </div>

      <div class="mb-6">
        <label class="block text-xs text-slate-300 font-semibold mb-1">North Atlantic Freshwater Influx (Sv = 10⁶ m³/s): <span id="val_hose" class="text-amber-400 font-bold">0.12 Sv</span></label>
        <input type="range" id="input_hose" min="0.00" max="0.40" step="0.01" value="0.12" class="w-full accent-amber-500" oninput="runSim08()">
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-4">
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-4 text-center">
          <div class="text-xs text-slate-400 uppercase">AMOC Overturning Volume Transport</div>
          <div id="out_amoc" class="text-3xl font-black text-emerald-400 my-1">16.4 Sv</div>
          <div id="out_amoc_state" class="text-xs text-emerald-300 font-bold">State: Active & Stable</div>
        </div>
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-4 text-center">
          <div class="text-xs text-slate-400 uppercase">Margin to Tipping Bifurcation</div>
          <div id="out_margin" class="text-2xl font-black text-cyan-400 my-1">0.14 Sv</div>
          <div class="text-xs text-slate-400">Critical Threshold: 0.26 Sv</div>
        </div>
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-4 text-center">
          <div class="text-xs text-slate-400 uppercase">Regional Climate Consequence</div>
          <div id="out_impact" class="text-sm font-bold text-slate-300 my-1">Normal European heat transport (+10°C anomaly maintained)</div>
        </div>
      </div>
    </div>
    <script>
      function runSim08() {
        const hose = parseFloat(document.getElementById('input_hose').value);
        document.getElementById('val_hose').innerText = hose.toFixed(2) + ' Sv';

        const crit = 0.26;
        const margin = Math.max(0, crit - hose);
        document.getElementById('out_margin').innerText = margin.toFixed(2) + ' Sv';

        const amocEl = document.getElementById('out_amoc');
        const stateEl = document.getElementById('out_amoc_state');
        const impactEl = document.getElementById('out_impact');

        if (hose < crit) {
          const transport = (19.0 - (hose / crit) * 6.5).toFixed(1);
          amocEl.innerText = transport + ' Sv';
          amocEl.className = 'text-3xl font-black text-emerald-400 my-1';
          stateEl.innerText = 'State: Active & Stable';
          stateEl.className = 'text-xs text-emerald-300 font-bold';
          impactEl.innerText = 'Normal North Atlantic heat transport. Monsoon circulation stable.';
        } else {
          amocEl.innerText = '2.1 Sv (COLLAPSED)';
          amocEl.className = 'text-3xl font-black text-red-400 my-1';
          stateEl.innerText = 'State: Tipped / Collapsed (Bistable Regime)';
          stateEl.className = 'text-xs text-red-300 font-bold';
          impactEl.innerText = '⚠️ Severe European cooling (-8°C), ITCZ shifts southward, severe Indian monsoon disruption.';
        }
      }
      setTimeout(runSim08, 100);
    </script>
    """
}

print("Simulators 5-8 loaded.")
