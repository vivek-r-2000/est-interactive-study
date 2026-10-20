# Simulators 9 to 12

SIMULATORS_3 = {
    "09": """
    <div class="eco-card p-6 border-emerald-800/60">
      <div class="flex items-center justify-between mb-4 pb-3 border-b border-emerald-900/60">
        <div>
          <h3 class="text-lg font-bold text-emerald-400">🌲 Terrestrial Carbon Sink & Soil Sequestration Calculator</h3>
          <p class="text-xs text-slate-300">Model carbon removal flux across afforestation hectares, biochar amendment, and soil organic carbon (SOC) conservation.</p>
        </div>
        <span class="badge-emerald px-2.5 py-1 rounded text-xs font-mono font-bold">Terrestrial Sinks</span>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
        <div>
          <label class="block text-xs text-slate-300 font-semibold mb-1">Afforestation Land Area (Million Hectares): <span id="val_aff" class="text-emerald-400 font-bold">25 Mha</span></label>
          <input type="range" id="input_aff" min="5" max="100" value="25" class="w-full accent-emerald-500" oninput="runSim09()">
        </div>
        <div>
          <label class="block text-xs text-slate-300 font-semibold mb-1">Biochar Amendment Rate (tonnes/ha): <span id="val_biochar" class="text-amber-400 font-bold">8 t/ha</span></label>
          <input type="range" id="input_biochar" min="0" max="30" value="8" class="w-full accent-amber-500" oninput="runSim09()">
        </div>
        <div>
          <label class="block text-xs text-slate-300 font-semibold mb-1">SOC Sequestration Rate (t C/ha/yr): <span id="val_soc" class="text-cyan-400 font-bold">0.6 t C/ha</span></label>
          <input type="range" id="input_soc" min="0.1" max="1.5" step="0.1" value="0.6" class="w-full accent-cyan-500" oninput="runSim09()">
        </div>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-4">
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-4 text-center">
          <div class="text-xs text-slate-400 uppercase">Annual CO₂ Sequestration Flux</div>
          <div id="out_ann_co2" class="text-3xl font-black text-emerald-400 my-1">0.48 Gt CO₂/yr</div>
          <div class="text-xs text-slate-400">Equivalent to ~15% of India emissions</div>
        </div>
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-4 text-center">
          <div class="text-xs text-slate-400 uppercase">30-Year Cumulative Carbon Storage</div>
          <div id="out_cum_co2" class="text-2xl font-black text-teal-400 my-1">14.4 Gt CO₂</div>
          <div class="text-xs text-slate-400">Living Biomass + Soil Pool</div>
        </div>
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-4 text-center">
          <div class="text-xs text-slate-400 uppercase">Permanence Rating</div>
          <div id="out_perm" class="text-lg font-bold text-amber-400 my-1">High (Biochar Weighted)</div>
          <div class="text-xs text-slate-400">&gt;500 year half-life component</div>
        </div>
      </div>
    </div>
    <script>
      function runSim09() {
        const aff = parseFloat(document.getElementById('input_aff').value);
        const bio = parseFloat(document.getElementById('input_biochar').value);
        const soc = parseFloat(document.getElementById('input_soc').value);
        document.getElementById('val_aff').innerText = aff + ' Mha';
        document.getElementById('val_biochar').innerText = bio + ' t/ha';
        document.getElementById('val_soc').innerText = soc.toFixed(1) + ' t C/ha';

        // aff in Mha (10^6 ha). Biomass uptake ~ 4.0 t CO2/ha/yr. SOC ~ soc * 3.67 t CO2/ha/yr. Biochar ~ bio * 2.8 t CO2/ha total amortized over 20 yr.
        const bio_yr = (bio * 2.8) / 20.0;
        const total_rate_per_ha = 4.0 + (soc * 3.67) + bio_yr;
        const total_annual_gt = (aff * 1e6 * total_rate_per_ha) / 1e9;
        const cum_30yr = total_annual_gt * 30.0;

        document.getElementById('out_ann_co2').innerText = total_annual_gt.toFixed(2) + ' Gt CO₂/yr';
        document.getElementById('out_cum_co2').innerText = cum_30yr.toFixed(1) + ' Gt CO₂';
      }
      setTimeout(runSim09, 100);
    </script>
    """,

    "10": """
    <div class="eco-card p-6 border-emerald-800/60">
      <div class="flex items-center justify-between mb-4 pb-3 border-b border-emerald-900/60">
        <div>
          <h3 class="text-lg font-bold text-emerald-400">🌊 Clean Development Mechanism (CDM) Additionality & Ocean Chemistry</h3>
          <p class="text-xs text-slate-300">Calculate Certified Emission Reductions (CERs), carbon finance revenue, and oceanic pH impact of deep-sea CO₂ sequestration.</p>
        </div>
        <span class="badge-emerald px-2.5 py-1 rounded text-xs font-mono font-bold">Carbon Markets</span>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
        <div>
          <label class="block text-xs text-slate-300 font-semibold mb-1">Baseline Emissions BE (tonnes CO₂/yr): <span id="val_be" class="text-emerald-400 font-bold">150,000</span></label>
          <input type="range" id="input_be" min="50000" max="500000" step="10000" value="150000" class="w-full accent-emerald-500" oninput="runSim10()">
        </div>
        <div>
          <label class="block text-xs text-slate-300 font-semibold mb-1">Project Emissions PE (tonnes CO₂/yr): <span id="val_pe" class="text-cyan-400 font-bold">35,000</span></label>
          <input type="range" id="input_pe" min="5000" max="250000" step="5000" value="35000" class="w-full accent-cyan-500" oninput="runSim10()">
        </div>
        <div>
          <label class="block text-xs text-slate-300 font-semibold mb-1">Carbon Credit Market Price ($/CER): <span id="val_price" class="text-amber-400 font-bold">$18</span></label>
          <input type="range" id="input_price" min="2" max="60" value="18" class="w-full accent-amber-500" oninput="runSim10()">
        </div>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-4">
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-4 text-center">
          <div class="text-xs text-slate-400 uppercase">Annual CERs Generated</div>
          <div id="out_cers" class="text-2xl font-black text-emerald-400 my-1">115,000 CERs</div>
          <div class="text-xs text-emerald-300 font-bold">✅ Additionality Proven (BE &gt; PE)</div>
        </div>
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-4 text-center">
          <div class="text-xs text-slate-400 uppercase">Annual Carbon Revenue</div>
          <div id="out_rev" class="text-2xl font-black text-amber-400 my-1">$2.07 Million</div>
          <div class="text-xs text-slate-400">Carbon offset market inflow</div>
        </div>
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-4 text-center">
          <div class="text-xs text-slate-400 uppercase">Deep Ocean Injection Local pH Drop</div>
          <div id="out_ph" class="text-2xl font-black text-red-400 my-1">-0.45 pH Units</div>
          <div class="text-xs text-slate-400">Corrosive to deep benthic calcifiers</div>
        </div>
      </div>
    </div>
    <script>
      function runSim10() {
        const be = parseFloat(document.getElementById('input_be').value);
        const pe = parseFloat(document.getElementById('input_pe').value);
        const price = parseFloat(document.getElementById('input_price').value);
        document.getElementById('val_be').innerText = be.toLocaleString();
        document.getElementById('val_pe').innerText = pe.toLocaleString();
        document.getElementById('val_price').innerText = '$' + price;

        const cers = Math.max(0, be - pe);
        const rev = (cers * price) / 1e6;
        const ph_drop = (0.2 + (cers / 500000) * 0.5).toFixed(2);

        document.getElementById('out_cers').innerText = cers.toLocaleString() + ' CERs';
        document.getElementById('out_rev').innerText = '$' + rev.toFixed(2) + ' Million';
        document.getElementById('out_ph').innerText = '-' + ph_drop + ' pH Units';
      }
      setTimeout(runSim10, 100);
    </script>
    """,

    "11": """
    <div class="eco-card p-6 border-emerald-800/60">
      <div class="flex items-center justify-between mb-4 pb-3 border-b border-emerald-900/60">
        <div>
          <h3 class="text-lg font-bold text-emerald-400">⚡ Direct Air Capture (DAC) & Clean Tech Energy Efficacy Evaluator</h3>
          <p class="text-xs text-slate-300">Compute net-carbon removal efficiency and energy penalties across solid sorbent and liquid solvent DAC systems.</p>
        </div>
        <span class="badge-emerald px-2.5 py-1 rounded text-xs font-mono font-bold">Clean Tech</span>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
        <div>
          <label class="block text-xs text-slate-300 font-semibold mb-1">Thermal Desorption Energy (GJ/t CO₂): <span id="val_thermal" class="text-amber-400 font-bold">5.5 GJ</span></label>
          <input type="range" id="input_thermal" min="3.0" max="9.0" step="0.5" value="5.5" class="w-full accent-amber-500" oninput="runSim11()">
        </div>
        <div>
          <label class="block text-xs text-slate-300 font-semibold mb-1">Electricity Input (kWh/t CO₂): <span id="val_elec" class="text-cyan-400 font-bold">350 kWh</span></label>
          <input type="range" id="input_elec" min="150" max="800" step="25" value="350" class="w-full accent-cyan-500" oninput="runSim11()">
        </div>
        <div>
          <label class="block text-xs text-slate-300 font-semibold mb-1">Grid Electricity Carbon Intensity (g CO₂/kWh): <span id="val_grid" class="text-emerald-400 font-bold">45 g</span></label>
          <input type="range" id="input_grid" min="0" max="800" step="20" value="45" class="w-full accent-emerald-500" oninput="runSim11()">
        </div>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-4">
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-4 text-center">
          <div class="text-xs text-slate-400 uppercase">Emissions Incurred by DAC Operation</div>
          <div id="out_oper_emiss" class="text-2xl font-black text-amber-400 my-1">62 kg CO₂/t</div>
          <div class="text-xs text-slate-400">Parasitic energy footprint</div>
        </div>
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-4 text-center">
          <div class="text-xs text-slate-400 uppercase">Net Carbon Removal Efficiency</div>
          <div id="out_net_eff" class="text-3xl font-black text-emerald-400 my-1">93.8%</div>
          <div class="text-xs text-emerald-300 font-bold">Net-Negative Verified</div>
        </div>
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-4 text-center">
          <div class="text-xs text-slate-400 uppercase">Levelized Cost of Removal</div>
          <div id="out_cost" class="text-2xl font-black text-teal-400 my-1">$485 / t CO₂</div>
          <div class="text-xs text-slate-400">Targeting &lt;$100 by 2040</div>
        </div>
      </div>
    </div>
    <script>
      function runSim11() {
        const thermal = parseFloat(document.getElementById('input_thermal').value);
        const elec = parseFloat(document.getElementById('input_elec').value);
        const grid = parseFloat(document.getElementById('input_grid').value);
        document.getElementById('val_thermal').innerText = thermal.toFixed(1) + ' GJ';
        document.getElementById('val_elec').innerText = elec + ' kWh';
        document.getElementById('val_grid').innerText = grid + ' g';

        const elec_emiss_kg = (elec * grid) / 1000.0;
        const thermal_emiss_kg = thermal * 8.5; // low carbon heat
        const total_incurred_kg = elec_emiss_kg + thermal_emiss_kg;
        const net_removal = Math.max(0, 1000.0 - total_incurred_kg);
        const net_eff = ((net_removal / 1000.0) * 100).toFixed(1);

        const cost = Math.round(300 + (thermal * 20) + (elec * 0.12) + (grid * 0.15));

        document.getElementById('out_oper_emiss').innerText = total_incurred_kg.toFixed(0) + ' kg CO₂/t';
        const effEl = document.getElementById('out_net_eff');
        effEl.innerText = net_eff + '%';
        if (parseFloat(net_eff) > 85) effEl.className = 'text-3xl font-black text-emerald-400 my-1';
        else if (parseFloat(net_eff) > 50) effEl.className = 'text-3xl font-black text-amber-400 my-1';
        else effEl.className = 'text-3xl font-black text-red-400 my-1';

        document.getElementById('out_cost').innerText = '$' + cost + ' / t CO₂';
      }
      setTimeout(runSim11, 100);
    </script>
    """,

    "12": """
    <div class="eco-card p-6 border-emerald-800/60">
      <div class="flex items-center justify-between mb-4 pb-3 border-b border-emerald-900/60">
        <div>
          <h3 class="text-lg font-bold text-emerald-400">📋 EIA Leopold Interaction Matrix & Impact Significance Evaluator</h3>
          <p class="text-xs text-slate-300">Evaluate developmental project actions against environmental receptors with interactive Magnitude and Importance scores.</p>
        </div>
        <span class="badge-emerald px-2.5 py-1 rounded text-xs font-mono font-bold">EIA Tool</span>
      </div>

      <div class="overflow-x-auto mb-6">
        <table class="w-full text-xs text-left text-slate-300 border border-emerald-900/80">
          <thead class="bg-[#05140d] text-emerald-400 uppercase text-[10px] tracking-wider border-b border-emerald-900">
            <tr>
              <th class="p-2 border-r border-emerald-900">Environmental Receptor</th>
              <th class="p-2 border-r border-emerald-900 text-center">Land Clearing (M / I)</th>
              <th class="p-2 border-r border-emerald-900 text-center">Excavation & Blasting (M / I)</th>
              <th class="p-2 border-r border-emerald-900 text-center">Wastewater Discharge (M / I)</th>
              <th class="p-2 text-center">Component Total Score</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-emerald-950 font-mono">
            <tr>
              <td class="p-2 font-sans font-bold text-slate-200 border-r border-emerald-900">Ambient Air Quality</td>
              <td class="p-2 text-center border-r border-emerald-900"><span class="text-amber-400">-4 / 6</span> (-24)</td>
              <td class="p-2 text-center border-r border-emerald-900"><span class="text-red-400">-7 / 8</span> (-56)</td>
              <td class="p-2 text-center border-r border-emerald-900"><span class="text-slate-400">0 / 0</span> (0)</td>
              <td class="p-2 text-center font-bold text-red-400">-80</td>
            </tr>
            <tr>
              <td class="p-2 font-sans font-bold text-slate-200 border-r border-emerald-900">Surface & Ground Water</td>
              <td class="p-2 text-center border-r border-emerald-900"><span class="text-amber-400">-3 / 5</span> (-15)</td>
              <td class="p-2 text-center border-r border-emerald-900"><span class="text-amber-400">-4 / 6</span> (-24)</td>
              <td class="p-2 text-center border-r border-emerald-900"><span class="text-red-400">-8 / 9</span> (-72)</td>
              <td class="p-2 text-center font-bold text-red-400">-111</td>
            </tr>
            <tr>
              <td class="p-2 font-sans font-bold text-slate-200 border-r border-emerald-900">Terrestrial Ecology & Flora</td>
              <td class="p-2 text-center border-r border-emerald-900"><span class="text-red-400">-9 / 9</span> (-81)</td>
              <td class="p-2 text-center border-r border-emerald-900"><span class="text-amber-400">-5 / 6</span> (-30)</td>
              <td class="p-2 text-center border-r border-emerald-900"><span class="text-slate-400">-1 / 3</span> (-3)</td>
              <td class="p-2 text-center font-bold text-red-400">-114</td>
            </tr>
            <tr>
              <td class="p-2 font-sans font-bold text-slate-200 border-r border-emerald-900">Local Employment & Economy</td>
              <td class="p-2 text-center border-r border-emerald-900"><span class="text-emerald-400">+5 / 6</span> (+30)</td>
              <td class="p-2 text-center border-r border-emerald-900"><span class="text-emerald-400">+6 / 7</span> (+42)</td>
              <td class="p-2 text-center border-r border-emerald-900"><span class="text-slate-400">0 / 0</span> (0)</td>
              <td class="p-2 text-center font-bold text-emerald-400">+72</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 mb-4">
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-4 text-center">
          <div class="text-xs text-slate-400 uppercase">Composite Leopold Score</div>
          <div class="text-3xl font-black text-red-400 my-1">-233</div>
          <div class="text-xs text-red-300 font-bold">Net Significant Adverse Impact</div>
        </div>
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-4 text-center">
          <div class="text-xs text-slate-400 uppercase">Statutory Category Mandate</div>
          <div class="text-xl font-bold text-amber-400 my-1">Category A (Central MoEFCC)</div>
          <div class="text-xs text-slate-400">Mandatory Public Hearing & EMP</div>
        </div>
        <div class="bg-[#06110d] border border-emerald-900/80 rounded-xl p-4 text-center">
          <div class="text-xs text-slate-400 uppercase">EMP Mitigation Budget Required</div>
          <div class="text-xl font-bold text-emerald-400 my-1">₹4.8 Crores (2.5% Project Cost)</div>
          <div class="text-xs text-slate-400">Zero Liquid Discharge (ZLD) + Greenbelt</div>
        </div>
      </div>
    </div>
    """
}

print("Simulators 9-12 loaded.")
